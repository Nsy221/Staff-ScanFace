import streamlit as st
from Home import face_rec
from datetime import datetime
import redis


def report():


    name = 'attendance:logs'
    # Retrieve the logs data and show in Report.py
    #extract data from redist list 

    
    def load_logs(name,end =-1):
        logs_list = face_rec.r.lrange(name, start=0,end=end) #extract all data from redis database
        return logs_list

    def delete_logs(name):
        
        # delete = face_rec.r.delete(name)
        
        # return delete # Success

        try:
            if face_rec.r.exists(name):
                delete = face_rec.r.delete(name)
                return delete  # Success
            else:
                print(f"Key'{name}' not found in Redis.")
                return False  # Key not found
        except Exception as e:
            print(f"Error deleting logs: {e}")
            return False  # Failure
        
      

    #tabs to show info
    tab1, tab2 = st.tabs(['Registered Data', 'Logs'])

    with tab1:
        if st.button('Refresh Data'):
            #Retrieve the Data from Redis Database
            with st.spinner('Retrieving Data from Redis DB ...'):
                redis_face_db = face_rec.retrieve_data(name='academy:register')
                st.dataframe(redis_face_db[['Name', 'Role']])


    with tab2:
        if st.button('Refresh Logs'):
            logs = load_logs(name=name)
            log_entries = []
            for log_entry in logs:
                try:
                    log_str = log_entry.decode("utf-8")  # Decode bytes to string
                    data = log_str.split('@')
                    if len(data) == 3:
                        name, role, timestamp_str = data
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
                        log_dict = {'Name': name, 'Role': role, 'Timestamp': timestamp}
                        log_entries.append(log_dict)
                    else:
                        st.warning(f"Invalid log entry format: {log_entry}")
                except Exception as e:
                    st.warning(f"Error parsing log entry: {log_entry}. Error: {e}")

            st.table(log_entries)


            # Add a button to delete logs
            # if st.button('Delete Logs'):
            #     delete_logs(name=name)
            #     st.success('Logs deleted successfully. Please refresh the page to see the changes.')

if __name__ == "__main__":
    report()


       