import shlex
import sys

def main() -> int:
    while true:
        users = 0
        userNames = [("name",0)]
        services= [][("service_name",0)]
        for i in range(0,users):
            strTable = "<html><table><tr><th>Service</th><th>Status</th></tr>"
            curtable = create_uset_table(userTuple,services)
            strTable = strTable + curtable;
        hs.open("usersTable.html",'w')
        hs.write(strTable)
        
        print(strTable)
        time.sleep(300)



def create_user_table(userTuple,services):
    number , name = userTuple
    banner = "<html><tr>name</tr>"
    strTable = "<html><table><tr><th>Service</th><th>Status</th></tr>"
    strTable = banner+strTable
    
    for num in range(0,5):
        serviceName,uptime =service_name[number][num]
        if uptime = 0:
            strRW = "<tr><td>"+ serviceName + "</td><td><style> body {background-color: red}"+uptime+"</style></td></tr>"
        else if uptime = 1:
            strRW = "<tr><td>"+ serviceName + "</td><td><style> body {background-color: green}"+uptime+"</style></td></tr>"
        strTable = strTable + strRW 
    return str
if __name__ == '__main__':
    sys.exit(main())