pragma solidity ^0.5.0;

import "./RewardsRTokens.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";


// Have the RewardsRTokensCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract RewardsRTokensCrowdsale is Crowdsale, MintedCrowdsale {
    
    // Provide parameters for all of the features of your crowdsale, such as the `rate`,
    //`wallet` for fundraising, and `token`.
    constructor(
        uint rate,
        address payable wallet,
        RewardsRTokens token
    )   
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor can stay empty
    }
}

contract RewardsRTokensCrowdsaleDeployer {

    address public rewards_r_tokens_address;
    address public rewards_r_tokens_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        // Create the RewardsRTokens and keep its address handy
        RewardsRTokens token = new RewardsRTokens(name, symbol, 0);
        rewards_r_tokens_address = address(token);

        // Create the RewardsRTokensCrowdsale and tell it about the token
        RewardsRTokensCrowdsale rewards_r_tokens_crowdsale = new RewardsRTokensCrowdsale(1, wallet, token);
        rewards_r_tokens_crowdsale_address = address(rewards_r_tokens_crowdsale);

        // make the RewardsRTokensCrowdsale contract a minter, then have the RewardsRTokensCrowdsaleDeployer
        // renounce its minter role
        token.addMinter(rewards_r_tokens_crowdsale_address);
        token.renounceMinter();
    }
}