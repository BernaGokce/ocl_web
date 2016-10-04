var UserSourcePage = function() {

    // user source locators
    this.newUserSrclink = element(by.id('new-user-source'));
    this.shortCode = $('#id_short_name');
    this.srcFullName = $('#id_full_name');
    this.supportedLocale = $('#id_supported_locales');
    this.customValidationType = $('#id_custom_validation_type');
    this.createUsrSourceButton = element(by.buttonText('Create Source'));

    this.clickNewUsrSrcLink = function () {
        this.newUserSrclink.click();
    };

    this.setShortCode = function (code) {
        this.shortCode.sendKeys(code);
    };

    this.setSrcFullName = function (full_name) {
        this.srcFullName.sendKeys(full_name);
    };

    this.setSupportedLocale = function (locale) {
       this.supportedLocale.sendKeys(locale)
    };

    this.setCustomValidationType = function (custom_validation_type) {
       this.customValidationType.sendKeys(custom_validation_type)
    };

    this.clickCreateUsrSrcButton = function () {
       this.createUsrSourceButton.click();
    };

    this.createNewUsrSource = function (code, full_name, locale, custom_validation_type){
        this.clickNewUsrSrcLink();
        this.setShortCode(code);
        this.setSrcFullName(full_name);
        this.setSupportedLocale(locale);
        this.setCustomValidationType(custom_validation_type);
        this.clickCreateUsrSrcButton();
    };
};
module.exports = UserSourcePage;
