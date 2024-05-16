/* eslint-disable */
import Currency from './3-currency.js';

export default class Pricing {
	constructor(amount, currency){
	  this.__amount = amount;
	  this.__currency = currency;
	}
	
	displayFullPrice(){
		return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
	}

	static convertPrice(amount, conversionRate) {
		return amount * conversionRate;
	}
	
	set amount(newAmount) {
    		this._amount = newAmount;
  	}

  	set currency(newCurrency) {
    		if (!(newCurrency instanceof Currency)) throw TypeError('currency must be an instance of Currency');
    		this._currency = newCurrency;
  	}

  	get amount() {
    		return this._amount;
  	}

 	get currency() {
	  	return this._currency;
	}
}
