#!/usr/bin/env python

def get_config():
	
	config = {
		'vault_token': '<your vault token>'
		,'vault_url': '<your vault url>'
		,'vault_secret': 'kv/secret/twitter'
		,'aws_dd_table': 'twitterdb'
	}
	
	return config
