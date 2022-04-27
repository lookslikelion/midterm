a = {}

a["이름"] = "김한준"
a["나이"] = "26살"
a["학번"] = "2016180028"
a["학과"] = "체육교육학과"
a["생일"] = "19971003"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print()

a = dict(이름 = "김한준", 나이 = "26살", 학번 = "2016180028", 학과 = "체육교육학과", 생일 = "19971003")
print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))