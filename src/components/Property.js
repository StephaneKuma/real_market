import React from 'react';

import { List, Card, Button, Icon } from 'antd';

import styles from '../CardList.less';

const gridStyle = {
    width: '25%',
    textAlign: 'center'
};

const Properties = (props) => {
    return (
        <List
            rowKey="id"
            grid={{ gutter: 24, lg: 3, md: 2, sm: 1, xs: 1 }}
            dataSource={props.data}
            renderItem={item =>
              item ? (
                <List.Item key={item.id}>
                  <Card hoverable className={styles.card} actions={[<a>操作一</a>, <a>操作二</a>]}>
                    <Card.Meta
                      avatar={<img alt="" className={styles.cardAvatar} src={item.avatar} />}
                      title={<a>{item.title}</a>}
                    />
                  </Card>
                </List.Item>
              ) : (
                <List.Item>
                  <Button type="dashed" className={styles.newButton}>
                    <Icon type="plus" /> 新建产品
                  </Button>
                </List.Item>
              )
            }
          />
    )
};

export default Properties;