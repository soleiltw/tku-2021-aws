import csv
import boto3


def main():
    print('Start')

    headers = ['name', 'grade']
    students = [{'name': 'john', 'grade': 80},
                {'name': 'george', 'grade': 90},
                {'name': 'anny', 'grade': 100}]

    file_name = '{}.csv'.format('english-grade')
    eng_grade_book = open(file_name, 'w')

    # create the csv writer object
    csv_writer = csv.writer(eng_grade_book)
    csv_writer.writerow(headers)
    for student in students:
        csv_writer.writerow([student['name'], student['grade']])

    eng_grade_book.close()

    bucket_name = 'YOUR-BUCKET-NAME-HERE'

    # Start with s3
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)

    download_url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket_name,
            'Key': file_name
        },
        ExpiresIn=10
    )
    if not download_url:
        print('Can\'t get the url.')
    else:
        print('CVS url is: {}'.format(download_url))


if __name__ == '__main__':
    main()
