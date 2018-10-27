const request = require('request-promise-native');

// request function that takes requestData as arg and makes the request
const onRequest = (requestData) => request(
  {
    method: requestData.method || 'GET',
    uri: `${window.location.origin}/${requestData.apiEndPoint}`,
    json: requestData.json || true,
    body: requestData.body || {},
    resolveWithFullResponse: requestData.resolveWithFullResponse || false,
  },
);

export default onRequest;

