import pika

def reconnect(self, queue_string):
    """
    Reconnect in case connection of the same object was closed
    """
    try:
        # context = ssl.create_default_context(cafile=CA_File)
        # context.load_cert_chain(client_certificate, private_key)
        # ssl_options = pika.SSLOptions(context, STAGE_LAMBDA_CYTEX)
        conn_params = pika.ConnectionParameters(
                        LAMBDA_NEW_CYTEX,
                        5672,
                        '/',
                        credentials = pika.PlainCredentials('stage', 'StgCtx@310A#'),
                        # ssl_options=ssl_options
                        )
        conn = pika.BlockingConnection(conn_params)
        self.channel = conn.channel()
        self.res=self.channel.queue_declare(queue=queue_string, durable=True)
        self.queue_string=queue_string
        return True
    except:
        return False