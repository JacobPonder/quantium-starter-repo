
from app import app


def Test_header(Dash):
    Dash.startserver(app)
    Dash.wait_for_element("#Header",timeout=20)



def Test_Visual(Dash):
    Dash.startserver(app)
    Dash.wait_for_element("#line_graph", timeout=20)

def Test_Radio(Dash):
    Dash.startserver(app)
    Dash.wait_for_element("#region", timeout=20)
