import React from 'react';
import { Route } from 'react-router-dom';

import PropertyListView from './containers/PropertyListView';
import PropertyDetailView from './containers/PropertyDetailView';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={PropertyListView} />
        <Route exact path='/:propertyID' component={PropertyDetailView} />
    </div>
);

export default BaseRouter;