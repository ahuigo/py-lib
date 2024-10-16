def log(func):
    def wrapper(*args, **kwargs):
        import pdb
        if len(args)>0:
            instance = args[0]
            if ' object ' in instance.__repr__():
                print("self_type:", instance.__class__.__name__, type(args[0]))
        print("func:", func, ) # <function A.echo at 0x1046c1e40>
        res = func(*args, **kwargs)
        return res
    return wrapper
class A:
    @log
    def echo(self, name="Alex"):
        print(f"echo {name}")
        return name

# bound method
a=A().echo
print(a.__repr__()) # <bound method A.echo of <__main__.A object at 0x1046c1e80>>

a.__self__.echo("Alex1")
a("Alex2")


