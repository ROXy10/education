import sys
string = sys.argv[1]
m = string.count("m")
w = string.count("w")
m_str = "m ({0}) {1}".format(m, "*"*m)
w_str = "w ({0}) {1}".format(w, "*"*w)
print(m_str+"\n"+w_str)