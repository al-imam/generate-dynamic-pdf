from datetime import datetime
import os
from xhtml2pdf import pisa
import requests

current_directory = os.path.dirname(os.path.abspath(__file__))


def convert_url_to_pdf(url, output_path):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        with open(output_path, 'wb') as pdf_file:
            pisa.CreatePDF(html_content, dest=pdf_file)
            print(f'PDF created at: {output_path}')
    else:
        print(f"Failed to retrieve HTML content from URL: {url}")


def convert_html_to_pdf(html_text, output_path):
    with open(output_path, 'wb') as pdf_file:
        pisa.CreatePDF(html_text, dest=pdf_file)
        print(f'PDF created at - {output_path}')

def wrap_space(value):
    return f"&nbsp;     <span style=\"font-family: sans-serif;\">{value}</span>     &nbsp;"


def get_html(name, passport):
    return f"""
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;  
      }}

      .main-container {{
        padding: 5px 50px;
        margin: 50px auto;
        font-size: 14px;
      }}

      h4 {{
        font-weight: 300;
        text-align: justify;
      }}
      
      .down-border {{
        text-decoration: underline;
        font-family: monospace;
      }}

      .underline {{
        text-decoration: underline;
      }}

      .up-border {{
        border-top: 2px solid black;
      }}

      .individual-container {{
        display: grid;
        grid-template-columns: repeat(2,1fr);
        column-gap: 50px;
        row-gap: 30px;
      }}

      .full-width-table {{
        width: 100%; 
        table-layout: fixed; 
      }}

      .style-tr {{
        display: block; 
        width: 100%;
      }}

      .style-td {{
        width: 47.5%; 
        padding: 2px 0 20px;
      }}

      .style-td-gap {{
        width: 5%;
        padding: 2px 0 20px;
      }}

      .style-td-down {{
        width: 47.5%; 
        padding: 2px 0 5px;
      }}


      .style-td-gap-down {{
        width: 5%;
        padding: 2px 0 5px;
      }}
      
      .description {{
        white-space: pre-wrap; 
        margin-bottom: 30px; 
        line-height: 1.6; 
        text-align: justify;
      }}

    </style>
  </head>
  
  <body style="font-family: sans-serif;">
    <div class="main-container">
      <table class="full-width-table">
        <tr class="style-tr">
          <td style="width: 50%; text-align: left;">Controller of Immigration<br /> Singapore </td>
          <td style="width: 50%; text-align: right;">Date: <span class="underline">{wrap_space(datetime.today().strftime('%Y-%m-%d'))}</span></td>
        </tr>
      </table>

      <h4 style="margin: 16px 0;">Dear Sir</h4>

      <h4 style="text-align: center; margin-bottom: 24px;">
        LETTER OF INTRODUCTION FOR VISA APPLICATION
      </h4>

      <p class="description"> The applicant for the visa, <span class="down-border">{wrap_space(str.upper(name))}</span> ( name of applicant ) of <span class="down-border">{wrap_space("BANGLADESH")}</span> ( country/place ), holder of passport/travel document no. <span class="down-border">{wrap_space(str.upper(passport))}</span> is coming to Singapore from <span class="down-border">{wrap_space("BANGLADESH")}</span> ( country/place of embarkation ) for the purpose of <span class="down-border">{wrap_space("HOLIDAY")}</span> ( e.g., holiday, transit, business, meeting, exhibition, visiting friends & relatives, employment, education for others, please specify ). The applicant is my <span class="down-border">{wrap_space("CLIENT")}</span>( e.g., father, mother, brother, sister, son, daughter, spouse, business partner; for others, please specify ). </p>

      <h4 style="margin: 30px 0;">
        Yours faithfully
      </h4>

      <h4 class="underline" style="padding-bottom: 40px; font-weight: bolder;">Only for application where Local Contact is an individual:</h4>

      <table class="full-width-table">

        <tr class="style-tr gap-top">
          <td class="up-border style-td">Signature of Local Contact</td>
          <td class="style-td-gap"></td>
          <td class="up-border style-td">NRIC (Pink / Blue) No</td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td">Name of Local Contact</td>
          <td class="style-td-gap"></td>
          <td class="up-border style-td">Contact Number</td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td-down">Address of Local Contact</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Email Address</td>
        </tr>
      </table>


      <h4 class="underline" style="font-weight: bolder;">Only for application where Local Contact is a company:</h4>

      <table class="full-width-table" style="margin-bottom: 60px:">
        <tr class="style-tr">
           <td style="text-align: center;"><img style="width: 100px;" src="data:image/jpeg;base64,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" alt="signature"></td>
          <td class="style-td-gap-down"></td>
          <td style="padding-bottom: 5px;"> <span style="font-weight: bold;">201727755Z</span> <span>&nbsp;&nbsp;&nbsp;</span> <img style="width: 100px;" src="data:image/jpeg;base64,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" alt="img"></td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td-down">Signature of person acting on behalf of the company/firm</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Signature of person acting on behalf of the
            company/firm</td>
        </tr>
        <tr class="style-tr">
          <td >SHAIKH MD SHAH JALAL, S7567880J, Director</td>
          <td class="style-td-gap-down"></td>
          <td >+65 98570429</td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td-down">Name, NRIC No. and Designation/Capacity</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Contact Number</td>
        </tr>
        <tr class="style-tr">
          <td >Flyasia Travel Pte Ltd. 92B sSyed Alwi Road (level 3),Singapore 207668</td>
          <td class="style-td-gap-down"></td>
          <td style="padding-top: 10px;">sgflyasia@gmail.com</td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td-down">Company Name and Address</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Email Address</td>
        </tr>
      </table>

      <p style="font-size: 18px;">
        V39A
      </p>
    </div>
  </body>
</html>
"""

def get_file_name(code):
    return f"{code}-visa-application.pdf"


def generate_pdf(name, passport, code):
    convert_html_to_pdf(get_html(name, passport), os.path.normpath(os.path.join(current_directory, "../generated", get_file_name(code))))
