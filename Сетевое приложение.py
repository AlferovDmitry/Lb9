import requests

base_url = "http://your_api_base_url/students/"

def update_student_data(student_id, updated_data):
    url = base_url + str(student_id) + "/"
    response = requests.put(url, json=updated_data)
    return response.json()

def delete_student_data(student_id):
    url = base_url + str(student_id) + "/"
    response = requests.delete(url)
    return response.json()
