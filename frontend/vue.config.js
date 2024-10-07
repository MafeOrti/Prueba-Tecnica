'use strict'
const path = require('path')
const pkg = require('./package.json')

function resolve(dir) {
  return path.join(__dirname, dir)
}

const name = pkg.name || 'pt' // page title
const port = 8080 // dev port

// All configuration item explanations can be find in https://cli.vuejs.org/config/
module.exports = {
  publicPath: '/',
  outputDir: '../backend/app/main/templates/dist',
  assetsDir: 'static',
  chainWebpack: (config) => {
    config.optimization.merge({
      splitChunks: { 
        automaticNameDelimiter: '-'
      }
    });
    config
      .plugin('html')
      .tap(args => {
        args[0].title = 'Static Web Apps Chat'
        return args
      })
  },
  configureWebpack: {
    devtool: 'source-map'
  },
}

