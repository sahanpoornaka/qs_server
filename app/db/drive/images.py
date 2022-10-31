from app.services.deta import get_deta


def get_drive():
    deta = get_deta()
    drive = deta.Drive("images")
    return drive
