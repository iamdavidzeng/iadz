const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
 
    /*入口*/
    entry: path.join(__dirname, '../src/index.js'),
    
    /*输出到dist目录，输出文件名字为bundle.js*/
    output: {
        path: path.join(__dirname, '../dist'),
        filename: 'bundle.js'
    },

    mode: "development",

    // 使用不同的loader对不同类型的文件进行处理。
    /*src目录下面的以.js结尾的文件，要使用babel解析*/
    /*src目录下面以.css结尾的文件，使用css相关插件进行整合*/
    /*cacheDirectory是用来缓存编译结果，下次编译加速*/
    module: {
        rules: [
            {
                test: /\.js$/,
                use: ['babel-loader?cacheDirectory=true'],
                include: path.join(__dirname, '../src')
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    // Old wrong config was:
                    // {
                    //     loader: "css-loader",
                    //     options: {
                    //         modules: true,
                    //         localIdentName: "[local]--[hash:base64:5]"
                    //     }
                    // }
                    {
                        loader: 'css-loader',
                        options: {
                            modules: {
                                localIdentName: '[local]--[hash:base64:5]'
                            }
                        }
                    },
                    {
                        loader: 'postcss-loader'
                    },
                ]
            },
            {
                test: /\.(png|jpg|gif)$/,
                use: [{
                    loader: 'url-loader',
                    options: {
                        limit: 8192
                    }
                }]
            }
        ]
    },

    // webpack-dev-server
    devServer: {
        // contentBase: path.join(__dirname, '../dist'), 
        compress: true,  // gzip压缩
        host: '0.0.0.0', // 允许ip访问
        hot:true, // 热更新
        historyApiFallback:true, // 解决启动后刷新404
        // proxy: {
        //     '/api': {
        //         target: 'http://localhost:8000',
        //         pathRewrite: {'^/api': ''},
        //         changeOrigin: true
        //     }
        // },
        port: 8000 // 端口
    },

    devtool: 'inline-source-map',

    // 定义别名
    resolve: {
        alias: {
            pages: path.join(__dirname, '../src/pages'),
            components: path.join(__dirname, '../src/components'),
            router: path.join(__dirname, '../src/router'),
            actions: path.join(__dirname, '../src/redux/actions'),
            reducers: path.join(__dirname, '../src/redux/reducers'),
            images: path.join(__dirname, '../src/images')
        }
    },

    // 所使用到的插件
    plugins: [
        new HtmlWebpackPlugin({
            filename: 'index.html',
            template: path.join(__dirname, '../public/index.html')
        })
    ],

};