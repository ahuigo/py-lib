import ldap3, base64

LDAP_CONFIG = {
    "ldap_host": "ldap://192.168.1.10:389",
    "bind_dn":"CN=<department>,OU=Account,DC=ahuigo,DC=com",
    "bind_pass": "passwd!",
    "base_dn": "OU=All Users,DC=ahuigo,DC=com",
    "search_user_filter":'(&(objectclass=person)(CN=%s))',
    "search_user_filter":'(&(objectclass=person))', # alluser
    "search_user_filter":'(&(objectClass=User)(objectCategory=Person))', # category
    # pgadmin:
    #   LDAP_SEARCH_FILETER='(objectclass=person)'
    #   LDAP_USERNAME_ATTRIBUTE='CN'
    #   self.username=person
    "attributes":['sAMAccountName'] #"scope": "users",
}

class AD(object):
    def __init__(self):
        self._connection = None
        self.ldap_host = LDAP_CONFIG.get('ldap_host')
        self.base_dn = LDAP_CONFIG.get('base_dn')
        self.bind_dn = LDAP_CONFIG.get('bind_dn')
        self.bind_pass = LDAP_CONFIG.get('bind_pass')
        self._server = self._get_server()


    def _get_server(self):
        return ldap3.Server(self.ldap_host, get_info=ldap3.ALL)

    def _get_connection(self):
        if not self._connection:
            self._connection = ldap3.Connection(self._server, self.bind_dn, self.bind_pass, auto_bind=True)

        else:
            try:
                self._connection.rebind() 
            except ldap3.core.exceptions.LDAPSocketSendError as e:
                self._connection = ldap3.Connection(self._server, self.bind_dn, self.bind_pass, auto_bind=True)
                
        return self._connection

    def login(self, username, passwd):
        connection = self._get_connection()
        search_res = connection.search(self.base_dn, '(&(objectclass=person)(CN=%s))' % username, attributes=LDAP_CONFIG.get('attributes'))

        if not search_res:
            return 'user_not_exists'

        try:
            entry_dn = connection.entries[0].entry_dn
            ldap3.Connection(self._server, entry_dn, passwd, auto_bind=True)
        except ldap3.core.exceptions.LDAPBindError as e:
            return 'invalid_password'

        return 'succ'

u = AD().login('user','pass')
print(u)


