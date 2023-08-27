from opensearchpy import OpenSearch
import boto3

def docsearch():
    opensearch_host = '10.0.77.10'
    opensearch_port = 9200
    opensearch_auth = ('admin', 'admin')
    client_id = 'testclientid'
    opensearch_index = client_id

    osc = OpenSearch(
        hosts = [{'host': opensearch_host, 'port': opensearch_port}],
        http_compress = True,
        http_auth = opensearch_auth,
        use_ssl = True,
        verify_certs = False,
        ssl_assert_hostname = False,
        ssl_show_warn = False
    )

    q = client_id
    query = {
      'size': 5,
      'query': {
        'multi_match': {
          'query': q,
          'fields': ['bucket', 'key']
        }
      }
    }

    response = osc.search(
        body = query,
        index = opensearch_index
    )

    ordresp = []
    qresponse = response['hits']['hits']
    for i in qresponse:
        ordresp.append(i['_source'])
    return(ordresp)

def add_file(client_id, file_id, file_name, file_to_upload):
    storage_url = 'http://10.0.77.10:9000'
    storage_class = 's3'
    client_id = 'mytestbucket'
    client_bucket = client_id
    client_index = client_id
    client_access_key = 'zJR3Z80D2QvAQTXe1huM'
    client_secret_key = 'dSyahEQWlWNh4UZTPQW56nCz5qgv3VyS0dOg79uy'
    client_doc_name = 'hello.txt'
    client_doc_tag = ''
    client_doc_url = ''
    storage_bucket = client_id
    opensearch_index = client_id

    s3c = boto3.client(storage_class, 
        endpoint_url=storage_url, 
        aws_access_key_id=client_access_key, 
        aws_secret_access_key=client_secret_key)

    s3c.upload_file(file_to_upload, 
        storage_bucket, 
        file_name)

    s3c_response = s3c.get_object(
        Bucket=storage_bucket, 
        Key=file_name)
    return s3c_response
