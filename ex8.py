formatter = "%s %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
 "I had this thing",
 "That u could type up right",
  "But id didn't sing.",
  "So I said good night"
)