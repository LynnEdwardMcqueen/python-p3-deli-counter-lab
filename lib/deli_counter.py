katz_deli = []


def line(organization_line):
    line_message = ""
    if len(organization_line) == 0:
        line_message = "The line is currently empty."
    else:
        line_message += "The line is currently:"
        i = 1
        for customer in organization_line:
            line_message += " " + str(i) + ". " + customer
            i += 1
    print (line_message)
    return

def now_serving(organization_line):
    if len(organization_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {organization_line.pop(0)}.")

def take_a_number(organization_line, new_customer):
    organization_line.append(new_customer)
    print(f"Welcome, {new_customer}. You are number {len(organization_line)} in line.")
    

line(katz_deli)
now_serving(katz_deli)
take_a_number(katz_deli, "Logan")
line(katz_deli)
take_a_number(katz_deli, "Lauren")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)

