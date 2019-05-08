import React from 'react';
import axios from 'axios';
import { Card } from 'antd'


class PropertyDetailView extends React.Component {
    state = {
        property: {}
    };

    componentDidMount() {
        const propertyID = this.props.match.params.propertyID;
        axios.get(`http://127.0.0.1:8000/properties/${propertyID}`)
            .then(res => {
                this.setState({
                    property: res.data
                });
                console.log(res.data)
            })
    }

    render() {
        return (
            <Card title={this.state.property.name}>
                <p>{this.state.property.property_desc}</p>
            </Card>
        )
    }
}

export default PropertyDetailView;