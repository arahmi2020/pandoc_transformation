from PyPDF2 import PdfReader
from enum import Enum
from docx import Document
from odf.opendocument import OpenDocumentText
from odf.text import P

from pathlib import Path

import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser("pdf_converter")
    parser.add_argument("-in", help="Path to the input folder.", dest='infolder', nargs=1, required=True, type=dir_path)
    parser.add_argument("-out", help="Path to the output folder.", dest='outfolder', nargs=1, required=True, type=dir_path)

    return parser.parse_args()

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

class FileTypes(Enum):
    DOCX = 1
    ODT = 2


def extractContent(filePath: str) -> str:
    """Extracts the content from the PDF file"""
    text = ""
    with open(filePath, "rb") as file:
        reader = PdfReader(file)
        for pageNumber in range(len(reader.pages)):
            page = reader.pages[pageNumber]
            text += page.extract_text()
    return text


def createDOCX(content: str, customPath: str) -> None:
    """Generates a DOCX file"""
    doc = Document()
    doc.add_paragraph(content)
    doc.save(customPath)


def createODT(content: str, customPath: str) -> None:
    """Generates a ODT file"""
    paragraph = P(text = content)
    doc = OpenDocumentText()
    doc.text.addElement(paragraph)
    doc.save(customPath)


def convert(content: str, customPath: str, type: FileTypes) -> None:
    """Converts the string to the defined type"""
    if type == FileTypes.DOCX:
        createDOCX(content, customPath)
    else:
        createODT(content, customPath)


def convertfile(filePath: str, customPath: str, type: FileTypes) -> None:
    """Converts the file to the defined type"""
    content = extractContent(filePath)
    if type == FileTypes.DOCX:
        createDOCX(content, customPath)
    else:
        createODT(content, customPath)

def main():
    parsed_args = parse_arguments()
    print (parsed_args)

    if parsed_args.infolder and parsed_args.outfolder:
        print(arparsed_argsgs.infolder)
        print(parsed_args.outfolderout)
        p = Path(parsed_args.infolder)
        y = [x for x in p.iterdir() if x.is_file()]
        print(y)


    #filePath = input("Insert path to pdf file:\n")
    #for 
    #convertfile(filePath, filePath + ".odt", FileTypes.ODT)
    #convertfile(filePath, filePath + ".docx", FileTypes.DOCX)

if __name__ == "__main__":
    main()
