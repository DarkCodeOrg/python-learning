People = {
    'first' : {
        "name" = "Alex",
        "Contact" = 100-200-300,
    },

    'Second' : {
        "name" = "marie",
        "Contact" = 101-202-333,
    }


}

for username, user_info in People:
    print("\nUsername " + username)
    name = user_info['name']
    Contact = user_info['Contact']
    