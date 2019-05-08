import React from 'react';
import axios from 'axios';

import Properties from '../components/Property';

const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    href: 'http://ant.design',
    title: `ant design part ${i}`,
    avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    description: 'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
  });
}

class PropertyListView extends React.Component {
    state = {
        properties: []
    };

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/properties/')
            .then(res => {
                this.setState({
                    properties: res.data
                });
                console.log(res.data)
            })
    }

    render() {
        return (
            <Properties data={listData} />
        )
    }
}

export default PropertyListView;