import React from 'react';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import PropertyListView from './containers/PropertyListView';

function App() {
    return (
        <div className="App">
            <CustomLayout>
                <PropertyListView />
            </CustomLayout>
        </div>
    );
}

export default App;
