exports.config = {
    framework: 'jasmine',
    seleniumAddress: 'http://localhost:9515',
    // seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['./specs/collections_spec.js'],
    capabilities: {
        'browserName': 'phantomjs'
        // 'browserName': 'chrome'
    },
    baseUrl: 'http://showcase.openconceptlab.org'
};
