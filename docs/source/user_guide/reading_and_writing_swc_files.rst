Reading and Writing SWC Files
=============================


Reading an SWC File
-------------------

The most common use case for ``swick`` is processing existing SWC files.

In order to accomplish that, of course we'll need some SWCs!
If you don't have any on hand, you can grab some at `NeuroMorpho.org <https://neuromorpho.org/index.jsp>`_ to follow along with this section.

Once you have an SWC file, you can read it into an :doc:`SWC object <../api_documentation/swc>` as follows: ::

  import swick

  # reads swc_file.swc into an object called my_swc
  my_swc = swick.read_swc('path/to/swc_file.swc')

.. note::
  
	The function :doc:`read_swc() <../api_documentation/io>` doubles as an SWC validator.
	If the provided SWC file is invalid, an exception will be provided specifying a line number and format issue.


Writing an SWC File
-------------------

Writing an SWC file is just as simple.

Let's expand on the above example to read an SWC file again, but this time to also write a copy of the read file to a new location: ::

  import swick

  # reads swc_file.swc into an object called my_swc
  my_swc = swick.read_swc('path/to/swc_file.swc')

  # writes a copy of swc_file.swc to a new file called new_copy.swc
  swick.write_swc('path/to/new_copy.swc', my_swc)

Obviously making copies of files is not a problem in need of solving.
The real fun of ``swick`` is in analyzing or modifying the SWC in between reading and writing; features we'll begin to explore in the next sections.
