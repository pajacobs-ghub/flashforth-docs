# Some FlashForth Documentation
This repository hosts the source for a collection of tutorial and 
reference documents for the [FlashForth](http://www.flashforth.com) 
programming environment for PIC and AVR microcontrollers.
These documents, in PDF format, are:

* Elements of FlashForth https://espace.library.uq.edu.au/view/UQ:321883
  An overview of the Forth language, as implemented by FlashForth.
  Although examples were done on a PIC18 microcontroller, 
  we have tried to abstract the discussion from particular hardware
  so that it is relevant to all FlashForth systems.
* A Tutorial Guide to Programming PIC18, PIC24 and AVR Microcontrollers with FlashForth
  https://espace.library.uq.edu.au/view/UQ:330707
  Here we have tried to provide motivational examples, tied to real hardware and exercises.
* FlashForth 5 Quick Reference for PIC and AVR Microcontrollers.
  https://espace.library.uq.edu.au/view/UQ:330706
  This should be good to have printed and on the desk when working with FlashForth.
  At least, that's how I use it.
  It works in a PDF viewer just as well, with the advantage of being easily searchable.

The latest versions can be built from this source collection.
Another benefit of cloning this repository is that the Forth sources 
for the examples are available in an easily copied form
(at least, easier than cutting and pasting from PDF files).

## Directory Contents
* `latex/`: The LaTeX source for the text of the reports. 
   The principal files are: 
    * `elements-of-flash-forth.tex` 
    * `ff5-tutorial-guide-2016.tex`
    * `flash-forth-5-quick-ref.tex`
* `figs/`: A directory of figures and photographs.  These are used to 
   illustrate the reports.
* `src/`: The Forth source and transcripts of the examples used 
   in the tutorial guide.
   Some of these files are copied from the FlashForth distribution to allow 
   this documentation set to be somewhat self-contained.
* `avr8/`: Forth code specific to the 8-bit Atmel's ATmega family 
   of microcontrollers.
* `arv8-2016`/: Some revised code for the ATmega examples.  
   Because the reports span some time and versions of the FlashForth system,
   we need different subdirectories to keep the like-named example files.
* `pic18/`: Forth code specific to the Microchip's 8-bit PIC18F microcontrollers.
* `pic24/`: Forth code specific to 16-bit PIC24F, dsPIC30 and dsPIC33 
   families of microcontrollers.
* `pdf/`: Definitive PDF versions that might be more up-to-date than
   the files in the UQespace archive.
 
## Building the Documents
I like to build the PDF documents with pdflatex, from within Kile.

## License
The source code is licensed with the GNU General Public License 3, 
consistent with FlashForth itself.
The documentation license is the Creative Commons 
Attribution-ShareAlike 4.0 International License.

## Chief Gardener
Peter Jacobs, 
School of Mechanical and Mining Engineering, 
The University of Queesnland.
