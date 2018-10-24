file_location = "nasa_data/Folder_SLFiles/access_log_Jul95"
ACCEPTED_EXTENSIONS = ["html", "htm"]

output_file_location = "nasa_data/processed_access_log_Jul95.csv"

# append file handler
fa = open(output_file_location, "a", encoding='utf8')

with open(file_location, "r", encoding='utf8', errors='ignore') as fr:
    error_count = 0
    success_count = 0
    line_count = 0
    http_errors_count = 0
    other_object_count = 0
    for line in fr:
        try:
            print('Processing: ' + line)
            line = line.strip()
            line_count += 1

            line_components = line.split(" ")
            host_name = line_components[0]
            date_time = line_components[3]
            item_requested = line_components[6]
            response_code = line_components[8]
            num_bytes = line_components[9]

            if str(response_code)[0] != "2":
                http_errors_count += 1
                continue
            else:
                # if the extension exists for the file
                position_of_last_period = item_requested.rfind(".")
                if position_of_last_period != -1:
                    extension = item_requested[position_of_last_period + 1:]
                    if extension not in ACCEPTED_EXTENSIONS:
                        other_object_count += 1
                        continue
            
            # remove the opening square bracket at the start
            date_time = date_time[1:]
            first_position_colon = date_time.index(":")
            date = date_time[:first_position_colon]
            time = date_time[first_position_colon + 1:]
            
            fa.writelines("{0},{1},{2},{3},{4}\n".format(host_name, date, time, item_requested, num_bytes))
            success_count += 1

        except Exception as ex:
            error_count += 1
            print("An error occurred while processing the line {0} due to {1}.".format(line, str(ex)))
    
    print("Line count: {0}".format(line_count))
    print("Number of errors: {0}".format(error_count))
    print("Number of successes: {0}".format(success_count))
    print("http_errors_count: {0}".format(http_errors_count))
    print("other_object_count: {0}".format(other_object_count))

fa.close()
        