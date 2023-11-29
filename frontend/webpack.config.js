
module.exports = {
    // other webpack configurations
  
    resolve: {
      fallback: {
        "stream": require.resolve("stream-browserify"),
        "util": require.resolve("util/")
      }
    }
  };