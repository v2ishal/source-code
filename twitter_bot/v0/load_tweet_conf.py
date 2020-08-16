#!/usr/bin/env python

def get_config():
	
	config = {
		'vault_token': 's.SgnDeKOTSkPWUhVyblEzreoE'
		,'vault_url': 'http://192.168.137.128:8200'
		,'vault_secret': 'kv/secret/twitter'
		,'aws_dd_table': 'twitterdb'
	}
	
	return config
