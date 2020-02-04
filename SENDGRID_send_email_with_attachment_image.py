#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:13:53 2020

@author: Bamwani
"""
import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient

message = Mail(
    from_email='sender@email.com',
    to_emails='receiver@email.com',
    subject='Test_with_attachment',
    html_content='test yo!')
file_path = 'filename.jpg'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/image')
attachment.file_name = FileName(str(file_path))
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('Example Content ID')
message.attachment = attachment
try:
    sendgrid_client = SendGridAPIClient('PASTE YOUR SENDGRID API HERE')
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except:
    pass
