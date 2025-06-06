def get_input():
    n = int(input())
    n_customer_list = list(map(int, input().split()))
    leader_customer,member_customer=map(int, input().split())
    return n, n_customer_list, leader_customer, member_customer


n, n_customer_list, leader_customer, member_customer = get_input()

cnt = 0
for n_customer in n_customer_list:
    n_customer -= leader_customer
    cnt += 1

    if n_customer > 0:
        x = n_customer // member_customer

        if n_customer % member_customer != 0:
            cnt += (x+1)
        else:
            cnt += x
    
print(cnt)
