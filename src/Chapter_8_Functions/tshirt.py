# create a function
def make_shirt(size='large', message='i love python'):
    print(f"Making you {size.title()} size shirt that says '{message.title()}'")
    
make_shirt('small', 'I love food')
make_shirt('medium')
make_shirt('small', 'i love java')