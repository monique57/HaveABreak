import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///haveabreak.db'  # Ensure this path is correct
    SQLALCHEMY_TRACK_MODIFICATIONS = False
