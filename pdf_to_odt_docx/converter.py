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


def extractContent(inFilePath: PurePath) -> str:
    """Extracts the content from the PDF file"""
    text = ""
    #with inFilePath.open() as f: f.readline()
    #with open(filePath, "rb") as file:
    with inFilePath.open() as file:
        reader = PdfReader(file)
        for pageNumber in range(len(reader.pages)):
            page = reader.pages[pageNumber]
            text += page.extract_text()
    return text


def createDOCX(content: str, outFilePath: PurePath) -> None:
    """Generates a DOCX file"""
    doc = Document()
    doc.add_paragraph(content)
    doc.save(str(outFilePath.absolute()))


def createODT(content: str, outFilePath: PurePath) -> None:
    """Generates a ODT file"""
    paragraph = P(text = content)
    doc = OpenDocumentText()
    doc.text.addElement(paragraph)
    doc.save(str(outFilePath.absolute()))


def convert(content: str, outFilePath: PurePath, type: FileTypes) -> None:
    """Converts the string to the defined type"""
    if type == FileTypes.DOCX:
        createDOCX(content, outFilePath)
    else:
        createODT(content, outFilePath)


def convertfile(inFilePath: PurePath, outFilePath: PurePath, type: FileTypes) -> None:
    """Converts the file to the defined type"""
    content: str = extractContent(inFilePath)
    if type == FileTypes.DOCX:
        createDOCX(content, outFilePath)
    else:
        createODT(content, outFilePath)

def main():
    parsed_args = parse_arguments()
    print (parsed_args)

    if parsed_args.infolder and parsed_args.outfolder:
        infolder = parsed_args.infolder[0]
        print(infolder)
        outfolder = parsed_args.outfolder[0]
        print(outfolder)
        p = Path(infolder)
        pdf_files = [x for x in p.iterdir() if x.is_file() and str(x).endswith('.pdf')]
        print(pdf_files)

        for pf in pdf_files:



    #filePath = input("Insert path to pdf file:\n")
    #for 
    #convertfile(filePath, filePath + ".odt", FileTypes.ODT)
    #convertfile(filePath, filePath + ".docx", FileTypes.DOCX)

if __name__ == "__main__":
    main()
