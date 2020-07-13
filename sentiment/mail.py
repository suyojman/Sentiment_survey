import base64

def send_email(filename):
    import os
    import json
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail,Attachment,FileContent, FileName, FileType, Disposition

    to_emails = [
        ('suyojman@gmail.com', 'Suyoj Man Tamrakar'),
        ('tamraksm@miamioh.edu', 'Sanjay Man Tamrakar')
    ]

    with open(filename, 'rb') as fd:
        encoded = base64.b64encode(fd.read()).decode()

    attachment = Attachment(
        FileContent(encoded),
    FileName(filename),
    FileType('text/csv'),
    Disposition('attachment')
    )
    print('Sendinggggggg')
    message = Mail(
        from_email=('suyoj.tamrakar@yipl.com.np', 'Suyoj Man Tamrakar'),
        to_emails=to_emails,
        subject='Sentiment Survey Past Results',
        html_content="<h2>These are the following details of the Sentiment Survey Past Results.</h2>"
                        " <h2>STAY HOME STAY SAFE </h2> ")
    message.attachment = attachment
    try:
        sendgrid_client = SendGridAPIClient('')
        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print('Errrrorrrrrrrrrr')
        print(e)
    return "Done"
