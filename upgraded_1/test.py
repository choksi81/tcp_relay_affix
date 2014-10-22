from repyportability import *
#from nmmain import *
add_dy_support(locals())
advertise = dy_import_module("advertise.r2py")
session = dy_import_module("session.r2py")
affix_stack = dy_import_module("affix_stack.r2py")

logging_affix_stack = affix_stack.AffixStack("(LoggingAffix)")


#answers=advertise.advertise_lookup("546")
try: 
  answers=advertise.advertise_lookup(579)
  #print answers
except advertise.AdvertiseError:
  #print "Error looking up 546"
  pass  
ip_port = answers[0]
#print ip_port
ip_port_list = ip_port.split(":")
#teststack = affix_stack.AffixStack("(TCPRelayAffix,192.168.0.2:12364)")
teststack = affix_stack.AffixStack("(TCPRelayAffix,"+ip_port+")(NamingAndResolverAffix,"Hello")") 
#tcp_forwarder = teststack.openconnection("192.168.0.2", 12354,my_ip,2374, 50)
tcp_forwarder = teststack.openconnection(ip_port_list[0],ip_port_list[1],my_ip,2374,50)
#tcp_forwarder = teststack.listenforconnection(ip_port_list[0], ip_port_list[1])
#remote_ip, remote_port, sockobj = tcp_forwarder.getconnection()
try:
  session.session_sendmessage(tcp_forwarder,"Hello")
  
except (sockettimeout.SocketTimeoutError, SocketClosedRemote, 
        session.SessionEOF), e:
  raise TCPServerSocketInvalidError("Cannotsend the message")
else:
  response = session.session_recvmessage(new_sockobj)
  print response

