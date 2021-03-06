pragma solidity ^0.4.19;

interface Sentinel {
  function payService(
    bytes32 _serviceName,
    address _from,
    address _to,
    uint256 _value)
      public;
}

contract VPNService {
  mapping(address => User) private users;

  struct User {
    uint256 dueAmount;
    VpnUsage[] vpnUsage;
  }

  struct VpnUsage {
    address addr;
    uint256 receivedBytes;
    uint256 sessionDuration;
    uint256 amount;
    uint256 timestamp;
    bool isPayed;
  }

  VpnUsage _vpnUsageTemplate;

  function addVpnUsage(
    address _addr,
    uint256 _receivedBytes,
    uint256 _sessionDuration,
    uint256 _amount,
    uint256 _timestamp)
      public {
        VpnUsage storage _vpnUsage = _vpnUsageTemplate;

        _vpnUsage.addr = msg.sender;
        _vpnUsage.receivedBytes = _receivedBytes;
        _vpnUsage.sessionDuration = _sessionDuration;
        _vpnUsage.amount = _amount;
        _vpnUsage.timestamp = _timestamp;
        _vpnUsage.isPayed = false;

        users[_addr].vpnUsage.push(_vpnUsage);
        users[_addr].dueAmount += _amount;
    }

  function payVpnSession(
    address _sentinelContractAddress,
    uint256 _amount,
    uint256 _sessionId)
      public {
        require(users[msg.sender].dueAmount >= _amount);
        require(users[msg.sender].vpnUsage[_sessionId].amount == _amount);
        require(users[msg.sender].vpnUsage[_sessionId].isPayed == false);

        address _to = users[msg.sender].vpnUsage[_sessionId].addr;
        Sentinel sentinel = Sentinel(_sentinelContractAddress);
        sentinel.payService('vpn', msg.sender, _to, _amount);

        users[msg.sender].dueAmount -= _amount;
        if ((users[msg.sender].vpnUsage[_sessionId].amount - _amount) == 0) {
          users[msg.sender].vpnUsage[_sessionId].isPayed = true;
        }
    }

  function getDueAmountOf(
    address _address)
      public constant returns(uint256) {
        return users[_address].dueAmount;
    }

  function getVpnSessionsOf(
    address _address)
      public constant returns(uint256) {
        return users[_address].vpnUsage.length;
    }

  function getVpnUsageOf(
    address _address,
    uint256 _sessionId)
      public constant returns(address, uint256, uint256, uint256, uint256, bool) {
        return (
          users[_address].vpnUsage[_sessionId].addr,
          users[_address].vpnUsage[_sessionId].receivedBytes,
          users[_address].vpnUsage[_sessionId].sessionDuration,
          users[_address].vpnUsage[_sessionId].amount,
          users[_address].vpnUsage[_sessionId].timestamp,
          users[_address].vpnUsage[_sessionId].isPayed
        );
    }
}
