import React, { ReactNode, useState } from 'react';
import {
  DesktopOutlined,
  FileOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
} from '@ant-design/icons';
import type { MenuProps } from 'antd';
import { Breadcrumb, Layout, Menu, theme, Image, Typography } from 'antd';
import { useNavigate } from 'react-router-dom';
import logo from "../icon.png";

const { Header, Content, Footer, Sider } = Layout;
const { Title } = Typography;

type MenuItem = Required<MenuProps>['items'][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[],
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
  } as MenuItem;
}


const items: MenuItem[] = [
  getItem('Home Page', '1', <PieChartOutlined />),
  getItem('Profile & Settings', '2', <UserOutlined />),
  getItem('Schedules', 'sub1',  <FileOutlined />, [
    getItem('Schedule - 1', '3'),
    getItem('Schedule - 2', '4'),
    getItem('Schedule - 3', '5'),
  ]),
];

interface LayoutProps {
    children: ReactNode;
  }

interface NavigationMap {
  [key: string]: string;
}

  const navigationMap: NavigationMap = {
    "1": '/home',
    "2": '/profile',
    "3": '/schedule/1',
    "4": '/schedule/2',
    "5": '/schedule/3',
  };

const MyLayout = (props: LayoutProps) => {
  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const navigate = useNavigate();

  return (
    <Layout style={{minHeight: '100vh'}}>
      <Sider collapsible collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
        <div style={{margin: '16px 0' }} >
          <Image src={logo} width={50} height={50} preview={false} />
          <Title level={5} style={{color: 'white', marginTop: '0px'}}>Schedule Creator</Title> 
        </div>
        <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} onClick={(event) => navigate(navigationMap[event.key].toString())}/>
      </Sider>
      <Layout className="site-layout">
        <Content style={{ margin: '0 16px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>User</Breadcrumb.Item>
          </Breadcrumb>
          <div style={{ padding: 24, background: colorBgContainer }}>
            {props.children}
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>ITU Scheduler ©2023 Created by ITU</Footer>
      </Layout>
    </Layout>
  );
};

export default MyLayout;