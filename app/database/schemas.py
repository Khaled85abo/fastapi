from pydantic import BaseModel, Field, ConfigDict, EmailStr


class CompanySchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="The name of the company, unique and required.")
    postal_code: str = Field( min_length=1, max_length=20, description="The postal code for the company's address. Optional.")
    email: EmailStr = Field( description="The contact email for the company. Optional and must be a valid email format.")
    description: str = Field( description="A description of the company. Optional.")
    analytics_module: bool = Field(None, description="Indicates whether the company uses the analytics module. Required.")
    company_type_id: int
		# json_schema_extra gör så att vår swagger-dokumentation visar ett exempel
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "name": "Tech University",
            "postal_code": "12345",
            "email": "info@techuniversity.com",
            "description": "A leading institution in technology education and research.",
            "analytics_module": True,
            "company_type_id": 1
        }
    })

class CompanyOutSchema(CompanySchema):
    id: int


class CompanyTypeSchema(BaseModel):
    name: str  = Field(... , min_length=1, max_length=50)
    model_config = ConfigDict(from_attributes=True)

class CompanyTypeOutSchema(CompanyTypeSchema):
    id: int