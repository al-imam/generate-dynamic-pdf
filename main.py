from io import BytesIO
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import  StreamingResponse
from jsonschema import ValidationError, validate
from src.generate_visa_pdf import get_visa_html
from src.generate_itenary_pdf import get_itenary_html
from xhtml2pdf import pisa
from src.schema import itenary_schema

app = FastAPI()

@app.post("/generate/visa/")
async def generate_pdf(request: Request):
    try:
        data = await request.json()

        if not (isinstance(data, dict) and data.get("name") and data.get("passport")):
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "'name' and 'passport' are required!",
                    "code": "invalid-req",
                },
            )

        pdf_buffer = BytesIO()

        try:
            content = get_visa_html(data.get("name"), data.get("passport"))
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail={
                    "message": f"PDF generation error: {str(e)}",
                    "code": "pdf-gen-error",
                },
            )

        return StreamingResponse(pdf_buffer, media_type="application/pdf")

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Request body is not valid JSON!",
                "code": "invalid-json",
            },
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Internal Server Error",
                "code": "server-break",
            },
        )



@app.post("/generate/itenary/")
async def generate_pdf(request: Request):
    try:
        data = await request.json()

        validate(data, itenary_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_itenary_html(data)
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail={
                    "message": f"PDF generation error: {str(e)}",
                    "code": "pdf-gen-error",
                },
            )

        return StreamingResponse(pdf_buffer, media_type="application/pdf")

    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Request doesn't contain valid data!",
                "expected-shape": {
                    "guests": [{"name": "string", "passport_no": "string"}],
                    "itenary": [
                        {"date": "2023-09-01", "from": "string", "to": "string"}
                    ],
                },
                "provided": data,
                "code": "invalid-request",
            },
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Request body is not valid JSON!",
                "code": "invalid-json",
            },
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Internal Server Error",
                "code": "server-break",
            },
        )
