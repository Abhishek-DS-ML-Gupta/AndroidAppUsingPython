Surakshak / Bharat App
======================

.. image:: screenshot.png
   :alt: Milky UI Screenshot

Overview
--------

**Surakshak / Bharat** is a modern, lightweight desktop application built using **Python Toga**.  
It demonstrates a **clean milky-themed UI** with buttons, labels, and a soft pastel design.  

This app is built to showcase **modern UI concepts** within the limitations of Toga while remaining **cross-platform**.

Features
--------

- Modern **milky-themed interface**
- Clean **soft pastel background**
- Primary and secondary buttons with subtle contrast
- Header, subtitle, and footer layout
- Fully **cross-platform using Toga & Briefcase**

Installation
------------

1. Clone the Repository:

   .. code-block:: bash

      git clone https://github.com/Abhishek-DS-ML-Gupta/AndroidAppUsingPython.git
      cd AndroidAppUsingPython

2. Create and Activate Virtual Environment:

   .. code-block:: bash

      # Windows
      python -m venv venv
      venv\Scripts\activate

      # Linux / Mac
      python -m venv venv
      source venv/bin/activate

3. Install Dependencies:

   .. code-block:: bash

      pip install -U toga briefcase

.. note::
   Toga may show dependency warnings for `requests` or `urllib3`. These are safe to ignore.

Running the App
---------------

Use **Briefcase** to run in development mode:

.. code-block:: bash

   briefcase dev

This will open the **Surakshak / Bharat app window** with the milky UI.

Project Structure
-----------------

.. code-block:: text

   BharatApp/
   ├── src/
   │   └── Bharat/
   │       ├── __init__.py
   │       └── app.py        # Main Toga app code
   ├── venv/                 # Python virtual environment
   ├── README.rst
   └── screenshot.png        # Optional screenshot

Usage
-----

- **Primary button**: Shows “Primary button clicked!” dialog  
- **Secondary button**: Shows “Secondary button clicked!” dialog  
- Layout demonstrates **vertical box with centered alignment**

Customization
-------------

You can customize the milky theme:

- **Background color**: change `outer_box` `background_color` in `app.py`  
- **Button colors**: update `background_color` and `color` in button styles  
- **Fonts and margins**: modify `Pack` attributes for `font_size`, `font_weight`, `margin`, etc.

Screenshots
-----------

.. image:: screenshot.png
   :alt: Milky UI Screenshot

Contributing
------------

Feel free to fork this repo and submit **pull requests**.  
Suggestions to improve **UI or add features** are welcome!

License
-------

MIT License © 2026 Abhishek Gupta
