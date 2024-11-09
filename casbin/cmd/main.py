import datetime
import casbin

e = casbin.Enforcer("../configs/model.conf", "../configs/policy.csv")

sub = "alice"     
obj = "data"     
act = "read"     
date_of_reg = datetime.datetime.now().isoformat()

# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if e.enforce(sub, obj, act, date_of_reg):
    print("Access granted")
else:
    print("Access denied")