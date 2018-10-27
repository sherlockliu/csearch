import TimeUtils from './timeUtils';

const store = require('store2');

const CACHE_DURATION = 24 * 60 * 60 * 1000; // one day.

class Cache {
  static add(key, data) {
    return store.add(key, {
      data,
      timeStamp: new Date().getTime(),
    });
  }

  static get(key) {
    return store.get(key) ? store.get(key).data : null;
  }

  static keys() {
    return store.keys();
  }

  static remove(key) {
    return store.remove(key);
  }

  static isExpired(key) {
    const data = store.get(key);
    if (data && data.timeStamp) {
      return TimeUtils.getDuration(new Date().getTime(), data.timeStamp) >= CACHE_DURATION;
    }
    return true; // true is expired
  }

  static includes(key) {
    return Cache.keys().includes(key) && !Cache.isExpired(key);
    // include key and not expired will return true
  }
}

export default Cache;
