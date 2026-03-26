import { useMemo, useState } from 'react';
import { AppContext } from './appContextCore.js';

export function AppProvider({ children }) {
  const [projectTitle, setProjectTitle] = useState('My React App');

  const value = useMemo(
    () => ({ projectTitle, setProjectTitle }),
    [projectTitle]
  );

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}
