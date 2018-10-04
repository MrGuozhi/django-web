# test

def _capture_screenshot(name):
    print(name)
    try:
        file_name = name.split("test_case/")[1]
        print(file_name)
    except IndexError:
        file_name = name
    base_dir = dirname(abspath(__file__))
    file_path = base_dir + "/test_report/image/" + file_name
    driver.save_screenshot(file_path)
