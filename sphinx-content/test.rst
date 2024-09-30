##################
Test of rst Syntax
##################

With an empty comment
---------------------

List:

-  .. 

      Quoted Block 1

         Quoted Block 2

Table:

.. list-table::

   * - ..

          Quoted Block 1

             Quoted Block 2

Syntax which works fine
-----------------------

Text:

   Quoted Block 1

      Quoted Block 2

List:

-  \ 

      Quoted Block 1

         Quoted Block 2

Table:

.. list-table::

   * - \ 

          Quoted Block 1

             Quoted Block 2


Quoted Block
------------

Text:

   Quoted Block 1

      Quoted Block 2

List with Block Quote
---------------------

The list:


-  |   Block 1.1 with Text line 1
   |   Block 1.1 with Text line 2
- 
   |   Block 1.2 with Text line 1
   |   Block 1.2 with Text line 2


List 2:

-     Block 2.1 with Text line 1

      Block 2.1 with Text line 2
-
      Block 2.2 with Text line 1

      Block 2.2 with Text line 2
-  Normal Text:

      Block 2.3 with Text line 1

      Block 2.3 with Text line 2
-  \ 

      Block 2.4 with Text line 1

      Block 2.4 with Text line 2

List 3:

- Block 3 with Text line 1

  Block 3 with Text line 2


List table with Block Quote
---------------------------

Table 1:

.. list-table::

   * -  |   Block 1.1 with Text line 1
        |   Block 1.1 with Text line 2
   * - 
        |   Block 1.2 with Text line 1
        |   Block 1.2 with Text line 2


Table 2:

.. list-table::

   * -    Block 2.1 with Text line 1

          Block 2.1 with Text line 2
   * -
          Block 2.2 with Text line 1

          Block 2.2 with Text line 2
   * - Normal Text:

          Block 2.3 with Text line 1

          Block 2.3 with Text line 2
   * - \ 

          Block 2.4 with Text line 1

          Block 2.4 with Text line 2

Table 3:

.. list-table::

   * - Block 3 with Text line 1

       Block 3 with Text line 2
