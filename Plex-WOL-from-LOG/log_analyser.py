import os
import re
from user import User
from ping3 import ping
from wakeonlan import send_magic_packet

class LogAnalyser:
    def __init__(self, active_users: list) -> None:
        self.target_ip_address = os.environ['IP_ADDRESS']
        self.mac_address = os.environ['MAC_ADDRESS']
        
        self.active_users = active_users
        self.request_regex = 'Request:'
        self.GET_regex = 'GET'
        self.connection_closed_regex = 'Completed after connection close'
        self.ip_address_regex = '\[([0-9]+(\.[0-9]+)+).*\]'
        self.id_regex = '\[.*(\d{5}).*\].*?GET'
        self.username_regex = 'Token.(\((.*?)\))'

    def check_for_new_user(self,line):
        if self._check_if_contains(line, self.request_regex) and self._check_if_contains(line, self.GET_regex):
            address = re.search(self.ip_address_regex, line)
            iD = re.search(self.id_regex, line)
            name = re.search(self.username_regex, line)

            if name and iD and address:
                new_user = User(address.group(1), iD.group(1), name.group(2))
                self._add_user_function(new_user)

            

        elif self._check_if_connection_close(line):
            address = re.search(self.ip_address_regex, line)
            iD = re.search(self.id_regex, line)
            user_to_remove = User(address.group(1), iD.group(1), None)

            self._remove_user_function(user_to_remove)

    def _check_if_contains(self, line, input_regex):
        value = re.findall(input_regex, line)
        if value:
            return True
        else:
            return False

    def _check_if_connection_close(self, line):
        value =  re.findall(self.connection_closed_regex, line)
        if value:
            return True
        else:
            return False

    def _add_user_function(self, new_user):
        if not self.active_users.get((new_user.address, new_user.id)):
            self.active_users.update({(new_user.address, new_user.id): new_user})
            print(f'New user ADDed: address-{new_user.address},id-{new_user.id},name-{new_user.name}')

        
        if not ping(self.target_ip_address, timeout = 2):
            send_magic_packet(self.mac_address, ip_address = self.target_ip_address)

    
    def _remove_user_function(self,user_to_remove):
        try:
            self.active_users.pop((user_to_remove.address, user_to_remove.id))
            print(f'EXIT user: address-{user_to_remove.address},id-{user_to_remove.id},name-{user_to_remove.name}')
        except:
            print('There was no user to delete')
        
