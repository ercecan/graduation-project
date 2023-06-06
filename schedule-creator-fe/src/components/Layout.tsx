import React, { ReactNode, useMemo, useState } from 'react';
import {
  BookOutlined,
  PieChartOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme, Image, Typography } from 'antd';
import { useNavigate } from 'react-router-dom';
import logo from '../icon.png';

const { Content, Footer, Sider } = Layout;
const { Title } = Typography;

interface MenuItem {
  key: React.Key;
  icon?: React.ReactNode;
  children?: MenuItem[];
  label: React.ReactNode;
}

function createMenuItem(
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
  };
}

interface LayoutProps {
  children: ReactNode;
}

interface NavigationMap {
  [key: string]: string;
}

const navigationMap: NavigationMap = {
  '1': '/home',
  '2': '/profile',
  '3': '/courses',
  // "3": '/schedule/1',
  // "4": '/schedule/2',
  // "5": '/schedule/3',
};

const MyLayout = (props: LayoutProps) => {
  const [collapsed, setCollapsed] = useState(false);
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const navigate = useNavigate();

  const jsonString = sessionStorage.getItem('schedules');
  const schedules = jsonString ? JSON.parse(jsonString) : [];

  const items = useMemo((): MenuItem[] => {
    const menuItems = schedules.map((schedule: any) => {
      navigationMap[schedule.id] = `/schedule/${schedule.id}`;
      return createMenuItem(schedule.name, schedule.id);
    });

    return [
      createMenuItem('Home Page', '1', <PieChartOutlined />),
      createMenuItem('Profile & Settings', '2', <UserOutlined />),
      createMenuItem('My Courses', '3', <BookOutlined />),
    ];
  }, []);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={(value) => setCollapsed(value)}
      >
        <div style={{ margin: '16px 0' }}>
          <Image src={logo} width={50} height={50} preview={false} />
          <Title level={5} style={{ color: 'white', marginTop: '0px' }}>
            Schedule Creator
          </Title>
        </div>
        <Menu
          theme="dark"
          defaultSelectedKeys={['1']}
          mode="inline"
          items={items}
          onClick={(event) => navigate(navigationMap[event.key].toString())}
        />
      </Sider>
      <Layout className="site-layout">
        <Content style={{ margin: '0 16px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}></Breadcrumb>
          <div style={{ background: colorBgContainer }}>{props.children}</div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          ITU Scheduler ©2023 Created by ITU
        </Footer>
      </Layout>
    </Layout>
  );
};

export default MyLayout;
