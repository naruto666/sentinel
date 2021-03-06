import json
import falcon
from ..eth import eth_manager
from ..eth import contract_manager


class CreateNewAccount(object):
    def on_post(self, req, resp):
        """
        @api {post} /client/account Create new account for the Sentinel user.
        @apiName CreateNewAccount
        @apiGroup Account
        @apiParam {String} password Password for creating the new account.
        @apiSuccess {String} account_addr New account address.
        @apiSuccess {String} private_key Private key of the account.
        @apiSuccess {String} keystore Keystore file data of the account.
        """
        password = str(req.body['password'])

        _, account_addr = eth_manager.create_account(password)
        _, private_key = eth_manager.get_privatekey(account_addr, password)
        _, keystore = eth_manager.get_keystore(account_addr)
        eth_manager.remove_keystore(account_addr)

        message = {
            'success': True,
            'account_addr': account_addr,
            'private_key': private_key,
            'keystore': json.dumps(keystore),
            'message': 'Account created successfully.' +
                       ' Please store the Private key and Keystore data safely.'
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(message)


class GetBalance(object):
    def on_post(self, req, resp):
        """
        @api {post} /client/account/balance Get account balance.
        @apiName GetBalance
        @apiGroup Account
        @apiParam {String} account_addr Address of the account.
        @apiSuccess {Object} balances Account balances.
        """
        account_addr = str(req.body['account_addr'])
        balances = {}

        error, balances['eths'] = eth_manager.get_balance(account_addr)
        if error is None:
            error, balances['sents'] = contract_manager.get_balance(account_addr)

        if error is None:
            message = {
                'success': True,
                'balances': balances
            }
        else:
            message = {
                'success': False,
                'error': error
            }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(message)
